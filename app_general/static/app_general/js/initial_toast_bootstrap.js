const toastTrigger = document.getElementById('liveToastBtn')
const toastLiveExample = document.getElementById('successToast')
if (toastTrigger) {
    toastTrigger.addEventListener('click', () => {
        const toast = new bootstrap.Toast(toastLiveExample)

        toast.show()
    })
}