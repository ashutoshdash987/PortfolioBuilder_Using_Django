const modalsOpen = document.querySelectorAll(".show-modal");
const modal = document.querySelector(".modall");
const overlay = document.querySelector(".overlay");
const modalclose = document.querySelector(".close-modal");

const openmodal = function () {
  modal.classList.remove("hidden");
  overlay.classList.remove("hidden");
};
const closemodal = function () {
  if (!modal.classList.contains("hidden")) {
    modal.classList.add("hidden");
    overlay.classList.add("hidden");
  }
};

// close modal using x sign
modalclose.addEventListener("click", closemodal);

// close modal by clicking outside the modal box
overlay.addEventListener("click", closemodal);

// close modal by pressing escape key
document.addEventListener("keydown", function (e) {
  if (e.key === "Escape") {
    closemodal();
  }
});
