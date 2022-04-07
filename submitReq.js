const firebaseConfig = {
  apiKey: "AIzaSyBGxvuoTqFrTcFfkSUSN8OakuI8f8slh-w",
  authDomain: "cadet-help.firebaseapp.com",
  databaseURL:
    "https://cadet-help-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "cadet-help",
  storageBucket: "cadet-help.appspot.com",
  messagingSenderId: "989944895209",
  appId: "1:989944895209:web:af5b936e74482a2a8a8278",
};
firebase.initializeApp(firebaseConfig);
var contactFormDB = firebase.database.ref("contactForm");
document.getElementById("contactForm").addEventListener("submit", submitForm);
function submitForm(e) {
  e.preventDefault();
  var name = getElementbyid("name");
  var email = getElementbyid("email"); //name,email,number,message
  var number = getElementbyid("number");
  var message = getElementbyid("message");

  console.log(name, email, number, message);
}
saveMessage(name, email, number, message);
const saveMessage = (name, email, number, message) => {
  var newContactForm = contactFormDB.push();
  newContactForm.set({
    name: name,
    email: email,
    message: message,
    number: number,
  });
};

const getElementbyid = (id) => {
  return document.getElementById(id).value;
};
