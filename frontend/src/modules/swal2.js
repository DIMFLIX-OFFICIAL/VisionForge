import Swal from "sweetalert2";

export function popup(title, msg, icon) {
    Swal.fire({
        icon: icon,
        title: title,
        text: msg,
        showConfirmButton: false,
        iconColor: "var(--lavander)",
        width: "30%",
        allowOutsideClick: true,
        backdrop: window.getComputedStyle(document.body).getPropertyValue('--bg') + '90'
    });
}

export function toast(title, icon) {
	const Toast = Swal.mixin({
		toast: true,
		position: "top",
		showConfirmButton: false,
		timer: 3000,
		timerProgressBar: true,
		didOpen: (toast) => {
			toast.onmouseenter = Swal.stopTimer;
			toast.onmouseleave = Swal.resumeTimer;
		}
	});
	Toast.fire({
		icon: icon,
		title: title,
		iconColor: "var(--lavander)"
	});
}

