const urlParams = new URLSearchParams(window.location.search);
const status = urlParams.get('status');
const msg = urlParams.get('msg');

if(status && msg){
    alert(msg);
    window.history.replaceState({}, document.title, window.location.pathname);
}
