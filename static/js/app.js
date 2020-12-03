$("#submit_button").on("click", function(){
    let age = $("#age").val()
    let birads = $("#birads").val()
    let HT = $("#HT").val()
    let FH = $("#FH").val()
    let MG = $("#MG").val()
    let BB = $("#BB").val()

    d3.json(`/data/${age}/${birads}/${HT}/${FH}/${MG}/${BB}`).then(data => {
        console.log(data)
        if (data.result = false){
            $("#result").html(`<h1>${"You can rest easy for it's unlikey that you have breast cancer."}<h1>`)
        } else{
            $("#result").html(`<h1>${"You might want to check your results with a doctor."}<h1>`)
        }
    })
})