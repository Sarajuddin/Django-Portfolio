// <!-- typed js effect starts -->
var typed = new Typed(".typing-text", {
    strings: ["Frontend Development", "Backend Development", "Web Designing", "Web Development", "AWS Services", "Cloud Computing"],
    loop: true,
    typeSpeed: 50,
    backSpeed: 25,
    backDelay: 500,
});
// <!-- typed js effect ends -->

function time_IP(){
    const dateTime = new Date();
    document.querySelector('input[id="time"]').value = dateTime;
    // console.log(dateTime);

    fetch("https://api64.ipify.org")
    .then((res)=> res.text())
    .then(ip => {
        document.querySelector('input[id="ip"]').value = ip
        // console.log(ip)
    })
    .catch(err=> console.log(err))
}
time_IP()

// Useful info...

// document.getElementById('browser').textContent = platform.name;
// document.querySelector('input[name="getBrowser"]').value = platform.name;
// document.querySelector('input[name="version"]').value = platform.version;
// document.querySelector('input[name="os"]').value = platform.os;
// document.querySelector('input[name="description"]').value = platform.description;