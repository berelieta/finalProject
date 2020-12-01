$("#submit_button").on("click", function(){
    let age = $("#age").val()
    let birads = $("#birads").val()
    let HT = $("#HT").val()
    let FH = $("#FH").val()
    let MG = $("#MG").val()
    let BB = $("#BB").val()

    d3.json(`/data/${age}/${birads}/${HT}/${FH}/${MG}/${BB}`).then(data => {
        console.log(data)
        // .val() = data
    })
})