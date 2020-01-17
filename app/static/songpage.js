/* 
Javascript used to format the user's song by making it look good on the front end

*/
let songContent = document.getElementById("content");
let song = songContent.innerText

function getTitle(text) {
    let title = "";
    for (i = 0; i < 15; i++) {
        if (text.charAt(i) != ":") {
            title += text.charAt(i);
        } else {
            return title;
        }
    }
}

// Removes Punctuation
function cleanSentance(sentance) {

    let firstCleaning = sentance.replace(/[\.,-\/#/!$%\^&\*;:{}=\-_`~()@\+\?><\[\]\+]/g, "");

    let secondCleaning = firstCleaning.replace(/\s{2,}/g, "");

    return finalCleaning(secondCleaning);
}

//Removes trailing apostrophes and unnecessary text
function finalCleaning(sentance) {
    sentance = sentance.replace(/'s/g, "");
    sentance = sentance.replace(/'t/g, "");
    sentance = sentance.replace(/'re/g, "");
    sentance = sentance.replace(/VERSE/g, "");
    return sentance.replace(/[0-9]/g, "");
}

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
            sentance = cleanSentance(sentance);
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
    document.getElementById("messagetext").style.visibility = "hidden";
}

let title = getTitle(song)
title = title.fontsize(7)
document.write(title + "<br> <br>")
song = song.replace(getTitle(song) + ":", "");
getStanzas(song)
hideMessage()