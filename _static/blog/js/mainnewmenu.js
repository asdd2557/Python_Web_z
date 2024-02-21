/* EXPANDER MENU */
const showMenu = (toggleId, navbarId, bodyId) => {
    const toggle = document.getElementById(toggleId),
        navbar = document.getElementById(navbarId),
        bodypadding = document.getElementById(bodyId)
        bodypaddingBackup = bodypadding.cloneNode(true);

    if (toggle && navbar) {
        toggle.addEventListener('click', () => {
            // Check if 'expander' class exists in the 'navbar'
            const isExpander = navbar.classList.contains('expander');

            // Toggle 'expander' class based on its current state
            if (isExpander) {
                navbar.classList.remove('expander');
                bodypadding.innerHTML = '';
            } else {
                navbar.classList.add('expander');
                if(bodypadding.innerHTML == '') {
                bodypadding.innerHTML = bodypaddingBackup.innerHTML;
                }

            }
        });
    }
}

showMenu('nav-toggle', 'navbar', 'body-pd');


/* LINK ACTIVE */
const linkColor = document.querySelectorAll('.nav__link')
function colorLink() {
    linkColor.forEach(l=> l.classList.remove('active'))
    this.classList.add('active')
}
linkColor.forEach(l=> l.addEventListener('click', colorLink))

/* COLLAPSE MENU */
const linkCollapse = document.getElementsByClassName('collapse__link')
var i

for(i=0;i<linkCollapse.length;i++) {
    linkCollapse[i].addEventListener('click', function(){
        const collapseMenu = this.nextElementSibling
        collapseMenu.classList.toggle('showCollapse')

        const rotate = collapseMenu.previousElementSibling
        rotate.classList.toggle('rotate')
    });
}


