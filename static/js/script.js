$(document).ready(function () {
    $(".sidenav").sidenav({edge: "right"});
    $('textarea#message').characterCounter();
    $('.collapsible').collapsible();
});

function sendMail(contactForm) {
    emailjs.send("service_sni5gk2", "template_ds0eavp", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.email.value,
        "message": contactForm.message.value
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
        },
        function(error) {
            console.log("FAILED", error);
        }
    );
    return alert("You're message has been sent!");
}
