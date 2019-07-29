// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
const printAppointment = (dogName, time, weather) =>{
if (isBerny(dogName) && noWalk(weather)) {
  return "I will walk berny at 12 in the " + weather;
}else{
  return "I will walk " + dogName + " at " + time;
}

}

const isBerny = (name) => {
  return name === "Berny";
}

const noWalk = (weather) => {
    return weather === "rain";
}






const sayHello = (dogName, time) => {

}



// Task 1
const dogName1 = "Steve";
const dogType1 = "beagle";

// Complete Task 1 Below
alert(printAppointment("Berny", "9", "rain"))
//
//
//
// const dogName2 = "Joe";
// const dogType2 = "bulldog";
//
// // Complete Task 2 Below
// if (dogType2 === "corgie") {
//   console.log("I will walk " + dogName2 +" at 12");
// } else {
//   console.log("I will walk " + dogName2 +" at 1");
// }
//
//
// const dogName3 = "Lola";
// const dogType3 = "poodle";
//
// // Complete Task 3 Below
//
// if (dogType3 === "corgie" || dogType3 === "beagle") {
//   console.log("I will walk " + dogName3 +" at 12");
// } else if (dogType3 === "bulldog") {
//   console.log("I will walk " + dogName3 + " at 1");
// } else {
//   console.log("I will walk " + dogName3 + " at 2");
// }
