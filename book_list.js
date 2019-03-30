"use strict";
$(document).ready(function() {

    $("#categories a").each(function() {
        var swappedImage = new Image();
        swappedImage.src = $(this).attr("href");
    });

    $("#categories h2").click(function(evt) {
        $(this).toggleClass("minus");
        if ($(this).attr("class") !== "minus") {
            $(this).next().hide();
        }
        else {
            $(this).next().show();
        }
$("#image").hide();

        evt.preventDefault();
    }); // end click

    $("#web_images a").click(function(evt) {
$("#image").show();
	var imageURL = $(this).attr("href");
	$("#image").attr("src", imageURL);

    evt.preventDefault();
    }); // end click

    $("#java_images a").click(function(evt) {
$("#image").show();
	var imageURL = $(this).attr("href");
	$("#image").attr("src", imageURL);

    evt.preventDefault();
    }); // end click
    $("#categories").find("a:first").focus();

    $("#net_images a").click(function(evt) {
$("#image").show();
	var imageURL = $(this).attr("href");
	$("#image").attr("src", imageURL);

    evt.preventDefault();
    }); // end click

    $("#database_images a").click(function(evt) {
$("#image").show();
	var imageURL = $(this).attr("href");
	$("#image").attr("src", imageURL);

    evt.preventDefault();
    }); // end click


}); // end ready