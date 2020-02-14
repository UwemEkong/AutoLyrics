/* 
Javascript used to format the user's song by making it look good on the front end

*/

let songContent = document.getElementById("content");
let song = songContent.innerText

//Formats the song into 5 stanzas
function getStanzas(text) {
    new_sentance_counter = 0;
    new_stanza_counter = 0;
    number_of_stanzas = 0;
    sentance = "";
    for (i = 0; i < text.length; i++) {

        if (number_of_stanzas == 5) {
            i = text.length;
        }

        if (text.charAt(i) == text.charAt(i).toUpperCase() && new_sentance_counter >= 4 && text.charAt(i) != " " && text.charAt(i + 1) != null) {
            document.write(sentance + "<br>")
            sentance = "";
            new_sentance_counter = 0;
            new_stanza_counter++
        }

        if (text.charAt(i) == " ") {
            new_sentance_counter++
        }

        if (new_stanza_counter >= 4) {
            document.write("<br>")
            new_stanza_counter = 0;
            number_of_stanzas++
        }

        sentance += text.charAt(i);
    }
}
// Hides original message 
function hideMessage() {
    document.getElementById("lyrics").style.visibility = "hidden";
}


hideMessage()
getStanzas(song)
