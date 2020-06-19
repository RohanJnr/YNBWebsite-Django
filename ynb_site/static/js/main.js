// NAVBAR ------------------------------------

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

// NAVBAR END -----------------------------------


// GALLERY

const categories = document.querySelector(".list-categories")

categoryList = [...categories.children]

categoryList.forEach(category => {
    category.addEventListener("click", listCategoryImages)
})

firstCategory = categories.firstElementChild
firstCategory.classList.add("active")

firstCategoryID = firstCategory.id

const categoryImages = document.getElementsByClassName(firstCategoryID)[0]


categoryImages.classList.add("active")

function listCategoryImages(e){
    if (!e.target.classList.contains("active")){
        const activeCategory = document.querySelector(".category.active")

        const activeCategoryImages = document.querySelector(".category-images.active")

        activeCategory.classList.remove("active")
        activeCategoryImages.classList.remove("active")

        e.target.classList.add("active")

        console.log(e.target.id)

        const requestedCategoryImages = document.getElementsByClassName(e.target.id)[0]

        requestedCategoryImages.classList.add("active")
    }
}

// GALLERY END -------------------------------------