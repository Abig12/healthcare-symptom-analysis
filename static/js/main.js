document.addEventListener("DOMContentLoaded", () => {
  const inputs = document.querySelectorAll('input[type="number"]');
  inputs.forEach((input) => {
    input.addEventListener("input", (e) => {
      const value = parseFloat(e.target.value);
      if (value < 0) e.target.value = 0;
      if (value > 1) e.target.value = 1;
    });
  });
});
