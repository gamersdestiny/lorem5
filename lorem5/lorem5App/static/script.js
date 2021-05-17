const bars = document.querySelector(".nav-bars");
const links = document.querySelector(".links");

bars.addEventListener("click", (e)=>{
	links.classList.toggle("shows")
});