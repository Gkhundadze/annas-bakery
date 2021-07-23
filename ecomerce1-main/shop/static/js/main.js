let searchInput = document.querySelector('#sinput')
let search = document.querySelector('.searchsvg');
let searchButton = document.querySelector('.searchButton');
let burgerBtn = document.querySelector('.burger-btn');
let accountsBnt = document.querySelector('.account-expand-arrow');
let navLinks = document.querySelector('.nav-links');
let itemAbout = document.querySelector('.item-about')
let account = document.querySelector('.account');
let receipt = document.querySelector('.receipt');
let shop = document.querySelector('.shop');
let expandMenu = document.querySelector('.account-expand');
let expandMenuReceipt = document.querySelector('.receipt-expand');
let expandMenuShop = document.querySelector('.shop-expand');
let socialSwitcher = document.querySelector('.social-icons-switcher');
let socialBox = document.querySelector('.social-links');

// brandBtn.addEventListener('click', () => {
//     brandsBox.classList.toggle('expanded-brand')
// })
if(account){
    account.addEventListener('click', () => {
        expandMenu.classList.toggle('d-block')
    })
}
if(receipt){
    receipt.addEventListener('click', () => {
        expandMenuReceipt.classList.toggle('d-block')
    })
}
if(shop){
    shop.addEventListener('click', () => {
        expandMenuShop.classList.toggle('d-block')
    })
}
if(accountsBnt){
    accountsBnt.addEventListener('click', () => {
        expandMenu.style.display = 'none'
    })
}
if(burgerBtn){
    burgerBtn.addEventListener('click', ()=> {
        // navLinks.classList.toggle("d-block")
        navLinks.classList.toggle('visible')
        navLinks.classList.toggle('special-margin')
        navLinks.classList.toggle("h-100")
        navLinks.classList.toggle('transparent')
        // navLinks.style.visibility = 'visible' 
        // navLinks.style.marginTop = '55px' 
        // navLinks.style.height = '100%' 
        itemAbout.classList.remove('ms-auto')
        
    })
    
}
if(socialSwitcher){
    socialSwitcher.addEventListener('click', () => {
        socialBox.classList.toggle('special-margin-social')
        socialSwitcher.classList.toggle('rotate-180')
    
    })
}
// searchInput.addEventListener('mouseover', () => {
//     search.style.transform = 'rotate(110deg)'
//     search.style.transition = '.5s ease-in'
//     searchInput.style.width = '500px'
//     searchInput.style.transition = '.3s ease-in'
// })
// searchInput.addEventListener('mouseleave', () => {
//     search.style.transform = 'rotate(0deg)'
//     search.style.transition = '.5s ease-out'
//     searchInput.style.width = '500px'
//     searchInput.style.transition = '.3s ease-in'
// })
// searchButton.addEventListener('mouseover', () => {
//     // searchInput.style.width = '200px'
// })



