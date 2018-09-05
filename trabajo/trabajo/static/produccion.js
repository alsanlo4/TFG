function opentab(evt, pestaña) {
    var i, tabcontent, tablinks;

    tabcontent = document.getElementsByClassName("tabcontent");

    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(pestaña).style.display = "block";
    evt.currentTarget.className += " active";
}

function ordenar()
{
    var display = document.getElementById("calidad").innerHTML;
    
    if(document.getElementById("year").innerHTML != "Año"){
        document.getElementById("year").innerHTML="Año";
    }
    
    if(display == "Calidad")
    {
        document.getElementById("calidad").innerHTML="Calidad &#8711";
        [].forEach.call(document.querySelectorAll('.papertables'),function (el) {
            el.style.display='none';});
        document.getElementById("paperDESC").style.display = 'block';
    }  
    else if(document.getElementById("paperDESC").style.display == 'block')
    {
        document.getElementById("calidad").innerHTML = "Calidad &#916";
        [].forEach.call(document.querySelectorAll('.papertables'),function (el) {
            el.style.display='none';});
        document.getElementById("paperASC").style.display = 'block';
    }
    else
    {
        [].forEach.call(document.querySelectorAll('.papertables'),function (el) {
            el.style.display='none';});
        document.getElementById("paper").style.display = 'block';
        document.getElementById("calidad").innerHTML = "Calidad";          
    }
}

function ordenaraño()
{
    var display = document.getElementById("year").innerHTML;

    if(document.getElementById("calidad").innerHTML != "Calidad"){
        document.getElementById("calidad").innerHTML="Calidad";
    }
    
    if(display == "Año")
    {
        document.getElementById("year").innerHTML="Año &#8711";
        [].forEach.call(document.querySelectorAll('.papertables'),function (el) {
            el.style.display='none';});
        document.getElementById("paperyearDESC").style.display = 'block';
    }  
    else if(document.getElementById("paperyearDESC").style.display == 'block')
    {
        [].forEach.call(document.querySelectorAll('.papertables'),function (el) {
            el.style.display='none';});
        document.getElementById("year").innerHTML = "Año &#916";
        document.getElementById("paperyearASC").style.display = 'block';
    }
    else
    {
        [].forEach.call(document.querySelectorAll('.papertables'),function (el) {
            el.style.display='none';});
        document.getElementById("paper").style.display = 'block';
        document.getElementById("year").innerHTML = "Año";          
    }
}




//Pruebas
/*$(document).ready(function()
{
    $("button").click(function()
    {   
        var texto = $(this).text();
        if(texto=="...")
        {
            $("button").html(".")
            $("p").show()
        }
        else{
            $("button").html("...")
            $("p").hide()}
    })
    
})*/

/*function first()
{
    document.getElementById("mensajeoculto").style.display = 'block';
    /*var display = document.getElementById("puntos").innerHTML;
    if(display == "...")
        document.getElementById("puntos").innerHTML=".";
    else
    {
        document.getElementById("puntos").innerHTML = "...";
        document.getElementById("mensajeoculto").style.display = 'none';    
    }*/
