//toggle menu mobile
document.addEventListener("DOMContentLoaded", () => {
    const buttonMobile = document.getElementById("button-mobile");
    const navBar = document.getElementById("navbar-content");
    const icon = document.getElementById("header-button-icon");
  
    buttonMobile.addEventListener("click", () => {
      navBar.classList.toggle("open");
  
      if (icon.classList.contains("bi-list")) {
        icon.classList.remove("bi-list");
        icon.classList.add("bi-x");
      } else {
        icon.classList.remove("bi-x");
        icon.classList.add("bi-list");
      }
    });
  });
  