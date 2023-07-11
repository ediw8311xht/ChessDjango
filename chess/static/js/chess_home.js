
import * as hl from "./helper_functions.js";

document.addEventListener('DOMContentLoaded', function() {
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    console.log("HI");
    console.log(csrftoken);
    console.log("BYE");
    let newgame_button = document.getElementById("new-game-button");

    newgame_button.addEventListener("click", (event) => {
        hl.post_request("", csrftoken);
    });

});

