//function for csrf token. from django
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


let btn = document.querySelectorAll(".cart-btn")
btn.forEach(btn=>{
    btn.addEventListener("click", addToCart)
})

async function addToCart(e){
    let product_id = e.target.value
    let url = "/cart/add_to_cart"
    let data = {id:product_id}
    console.log(product_id)

    await fetch(url, {
        method: "POST",
        headers:{"content-type":"application/json", 'X-CSRFToken': csrftoken},
        body: JSON.stringify(data)
    })
    .then(res=>res.json())
    .then(data=>{
        if (data.success) {
            location.reload();
        } else if (data.redirect_url) {
            location.reload();
            window.location.href = data.redirect_url;
        }
        console.log(data)
    })
}


//code for increase, decrease and remove
const buttons = document.querySelectorAll(".quantity-button");
buttons.forEach(button => {
    button.addEventListener("click", function (e) {
        console.log("Button clicked!");
        let product_id = e.target.value; // Access the "data-product-id" attribute
        let url = "/cart/update";
        let action = this.dataset.action;
        let data = { id: product_id, action: action };
        console.log(product_id, action);

        fetch(url, {
            method: "POST",
            headers: { "content-type": "application/json", 'X-CSRFToken': csrftoken },
            body: JSON.stringify(data)
        })
        .then(res => res.json())
        .then(data => {
            console.log(data);
            location.reload();
        });
    });
});