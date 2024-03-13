 

jQuery(function($){
    $('.pluscart').click(function(){
        var id = $(this).attr("pid").toString();
        var ele = document.getElementById(id).value;
        var newval = parseInt(ele) + 1;
        
        console.log(ele)
        $.ajax({
            type:"GET",
            url:"/pluscart",
            data:{
                prod_id:id
            },
            success:function(data){
                console.log("data = ", data)
                document.getElementById(id).value = data.quantity;
                document.getElementById("amount").value = data.total;
                document.getElementById("cart-total").innerHTML = data.t;
            }
        })
    }) 
})

jQuery(function($){
    $('.minuscart').click(function(){
        var id = $(this).attr("pid").toString();
        var ele = document.getElementById(id).value;
        var newval = parseInt(ele) - 1;
        
        console.log(ele)
        $.ajax({
            type:"GET",
            url:"/minuscart",
            data:{
                prod_id:id
            },
            success:function(data1){
                console.log("data = ", data1)
                document.getElementById(id).value = data1.quantity;
                document.getElementById("amount").value = data1.total;
                document.getElementById("cart-total").innerHTML = data1.t;

            }
        })
    }) 
})

jQuery(function($){
    $('.removecart').click(function(){
        var id = $(this).attr("pid").toString();
        var ele = this;
        var newval = parseInt(ele) - 1;
        
        console.log(ele)
        $.ajax({
            type:"GET",
            url:"/removecart",
            data:{
                prod_id:id
            },
            success:function(data2){
                console.log("data = ", data2)
                ele.parentNode.parentNode.parentNode.remove();
                document.getElementById("amount").value = data2.total;
                console.log(data2.t)
                document.getElementById("cart-total").innerHTML = data2.t;
            }
        })
    }) 
})
