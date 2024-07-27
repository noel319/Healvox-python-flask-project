# Flask modules
from flask import Blueprint, redirect, url_for, flash, render_template, request, flash
from flask_login import login_required, current_user
from flask_login import login_user, logout_user, login_required
from flask_mail import Message
from werkzeug.security import generate_password_hash, check_password_hash
import random

# Other modules
import logging

# Local modules
from app.models.auth import User
from app.extensions import db, bcrypt, limiter, mail

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/login", methods=["GET", "POST"])
@limiter.limit("60/minute")
def login():   
    if current_user.is_authenticated:
        return redirect(url_for("pages.core.home_route"))

    else:
        if request.method=='POST' :
            email =request.form['email-login']
            password= request.form['password-login']
            user = User.query.filter_by(email=email).one_or_none()        
            if user and bcrypt.check_password_hash(user.password, password):
                if user.is_active:
                    login_user(user)           
                    return redirect(url_for("pages.core.home_route"))
                else:
                    flash('Please verify your email before logging in.', 'warning')
                    return redirect(url_for('auth.verify_email'))
            flash('Invalid credentials, please try again.','danger')
        else:
            return render_template("auth/login.html")


@auth_bp.route("/register", methods=["GET", "POST"])
@limiter.limit("30/minute")
def register():
    if current_user.is_authenticated:
        return redirect(url_for("pages.core.home_route"))
        
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    hashed_password = bcrypt.generate_password_hash(password)

     # Generate a random 6-digit verification code
    verification_code = f"{random.randint(100000, 999999)}"

    # Add user to database
    new_user = User(name=name, email=email, password=hashed_password, verification_code=verification_code)
    db.session.add(new_user)
    db.session.commit()

    msg = Message('Confirm Your Email', recipients=[email])
    msg.body = f'Your verification code is {verification_code}'
    mail.send(msg)
        # Login user
    login_user(new_user)

    flash(
        f"Account created successfully! You are now logged in as {new_user.name}.",
        "success",
    )
    flash('A verification email has been sent to your email address. Please enter the code to complete registration.', 'info')
    return redirect(url_for('auth.verify_email'))   

# Email Verification Route
@auth_bp.route('/verify_email', methods=['GET', 'POST'])
@limiter.limit("1/minute")
def verify_email():
    if request.method =='POST':
        email = request.form['email']
        code = request.form['code']

        user= User.query.filter_by(email=email).first()

        if user and user.verification_code == code:
            user.is_active = True
            # Clear the verification code after successful verification
            user.verification_code = None
            db.session.commit()
            flash('Your account has been confirmed!', 'success')
            return redirect(url_for('auth.login'))
        else:
            flash('Invalid verification code. Please try again.', 'danger')
    return render_template('verify_email.html')

@auth_bp.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
