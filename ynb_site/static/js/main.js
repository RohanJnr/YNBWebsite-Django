const hamburgerMenu = document.getElementById("hamburger-menu")

const navLeft = document.getElementById("nav-left")

const navRight = document.getElementById("nav-right")

const expandedClassName = "expanded"

// expand navbar when hamburger menu triggers a click event.
hamburgerMenu.addEventListener("click", showNavbar)

function showNavbar(e) {
    e.target.classList.toggle(expandedClassName)
    navLeft.classList.toggle(expandedClassName)
    navRight.classList.toggle(expandedClassName)
}
