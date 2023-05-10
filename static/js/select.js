let select = document.getElementById('payment');
let bankBillForm = document.getElementById('bank-bill')
let creditCardForm = document.getElementById('credit-card')


select.addEventListener("change", function() {
    if (select.value == "credit") {
        creditCardForm.classList.remove('zero')
        bankBillForm.classList.add('zero')
    }
    else {
        creditCardForm.classList.add('zero')
        bankBillForm.classList.remove('zero')
    }
})