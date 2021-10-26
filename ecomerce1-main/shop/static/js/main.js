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
let shopIsOpen = false;
let accountIsOpen = false;
let receiptIsOpen = false;
let cart = document.querySelector('.cart')
let cartCounter = document.querySelector('.cart-caunter')


// LOGIN
// const loginBtn = document.querySelector('.login-link')
// const loginIframe = document.querySelector('.login-iframe')
// const closeIframe = document.querySelector('close-login-modal')
// let loginForm = document.querySelector('.login-form')
// if(loginBtn){
//     loginBtn.addEventListener('click', (e)=> {
//         e.preventDefault();
//         loginIframe.style.display = 'block'
//         closeIframe.addEventListener('click', ()=>{
//             alert('closed')
//             loginIframe.style.display = 'none'
//         })

//     })
// }


// LOGIN



// REGISTER
// const registerBtn = document.querySelector('.register-link')
// const registerIframe = document.querySelector('.register-iframe')
// if(registerBtn){
//     registerBtn.addEventListener('click', (e)=> {
//         e.preventDefault();
//         registerIframe.style.display = 'block'
//         console.log('register clicked' + registerIframe);
//     })
// }

// REGISTER



// brandBtn.addEventListener('click', () => {
//     brandsBox.classList.toggle('expanded-brand')
// })
if(cart){
    cart.addEventListener('click', ()=>{
        if(cartCounter.innerHTML == 0){
            alert('კალათა ცარიელია')
        }
        
    })
}
document.addEventListener('click', (e)=>{
    if(e.target !== shop && e.target !== account && e.target !== receipt){
        expandMenuShop.style.display = 'none';
        shopIsOpen = false;
        expandMenu.style.display = 'none';
        accountIsOpen = false;
        expandMenuReceipt.style.display = 'none';
        receiptIsOpen = false;
    }else{
        if(e.target == shop){
            if(accountIsOpen || receiptIsOpen){
                expandMenu.style.display = 'none';
                accountIsOpen = false;
                expandMenuReceipt.style.display = 'none';
                receiptIsOpen = false;
            }
        }
        else if(e.target == account){
            if(shopIsOpen || receiptIsOpen){
                expandMenuShop.style.display = 'none';
                shopIsOpen = false;
                expandMenuReceipt.style.display = 'none';
                receiptIsOpen = false;
            }
        }
        else if(e.target == receipt){
            if(shopIsOpen || accountIsOpen){
                expandMenuShop.style.display = 'none';
                shopIsOpen = false;
                expandMenu.style.display = 'none';
                accountIsOpen = false;
            }
        }
    }
})
if(account){
    account.addEventListener('click', () => {
        if(accountIsOpen == false){
            expandMenu.style.display = 'block';
            accountIsOpen = true;
        }else{
            expandMenu.style.display = 'none';
            accountIsOpen = false;
        }
    })
}
if(receipt){
    receipt.addEventListener('click', () => {
        if(receiptIsOpen == false){
            expandMenuReceipt.style.display = 'block';
            receiptIsOpen = true;
        }
        else{
            expandMenuReceipt.style.display = 'none';
            receiptIsOpen = false;
        }
    })
}
if(shop){
    shop.addEventListener('click', () => {
        if(shopIsOpen == false){
            expandMenuShop.style.display = 'block';
            shopIsOpen = true;
        }else{
            expandMenuShop.style.display = 'none';
            shopIsOpen = false;
        }


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



