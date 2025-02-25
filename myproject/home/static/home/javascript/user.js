function toggleDropdown() {
    const userLogin = document.querySelector('.user-login');
    userLogin.classList.toggle('active');
}

// Đóng dropdown khi click ra ngoài
window.onclick = function(event) {
    if (!event.target.closest('.user-login')) {
        document.querySelector('.user-login').classList.remove('active');
    }
}
