/* EXPANDER MENU */
const showMenu = (toggleId, navbarId, bodyId, extraId) => {
    const toggle = document.getElementById(toggleId),
        navbar = document.getElementById(navbarId),
        extra = document.getElementById(extraId)
        extraBackup = extra.cloneNode(true);

    if (toggle && navbar) {
        toggle.addEventListener('click', () => {
            // Check if 'expander' class exists in the 'navbar'
            const isExpander = navbar.classList.contains('expander');

            // Toggle 'expander' class based on its current state
            if (isExpander) {
                navbar.classList.remove('expander');
                extra.innerHTML = '';
            } else {
                navbar.classList.add('expander');
                if(extra.innerHTML == '') {
                extra.innerHTML = extraBackup.innerHTML;
                }

            }
        });
    }
}

showMenu('nav-toggle', 'navbar', 'body-pd', 'extra-content');


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


