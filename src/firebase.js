// For Firebase JS SDK v7.20.0 and later, measurementId is optional
import firebase from "firebase/compat/app";
import "firebase/compat/auth";
import "firebase/compat/firestore";

const firebaseConfig = {
  apiKey: "AIzaSyCR9QnER7kb4T-CZE3vTVX4EyUnu7MkqYE",
  authDomain: "price-deck.firebaseapp.com",
  projectId: "price-deck",
  storageBucket: "price-deck.appspot.com",
  messagingSenderId: "668316657045",
  appId: "1:668316657045:web:aa4dc63687b5da286dc29c",
  measurementId: "G-1YT6MF8VFK",
};

const firebaseApp = firebase.initializeApp(firebaseConfig);
const db = firebaseApp.firestore();
const auth = firebaseApp.auth();
const provider = new firebase.auth.GoogleAuthProvider();

export { auth, provider };
export default db;
