// Nickolas Kavanagh
// SD 12 QAP 4
// Project 3 – JavaScript
// July 15, 2024 - July 26, 2024

const motelCustomer = {
    name: "Nick Kavanagh",
    birthDate: new Date("1996-06-15"),
    gender: "Male",
    roomPreferences: ["non-smoking", "king-sized bed", "room service"],
    paymentMethod: "Credit Card",
    mailingAddress: {
      street: "123 Main St",
      city: "Goulds",
      province: "NL",
      postalCode: "A1S 1H2"
    },
    phoneNumber: "(123) 456-7890",
    stay: {
      checkIn: new Date("2023-07-14"),
      checkOut: new Date("2023-07-26")
    },
    
    getAge() {
        const today = new Date();
        let age = today.getFullYear() - this.birthDate.getFullYear();
        const monthDiff = today.getMonth() - this.birthDate.getMonth();
        if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < this.birthDate.getDate())) {
          age--;
        }
        return age;
      },
      
      getDurationOfStay() {
        const oneDay = 24 * 60 * 60 * 1000; // milliseconds in a day
        return Math.round((this.stay.checkOut - this.stay.checkIn) / oneDay);
      }
    };
    
    // Template literal string describing the customer
    const customerDescription = `
    Our valued customer, ${motelCustomer.name}, is a ${motelCustomer.getAge()}-year-old ${motelCustomer.gender.toLowerCase()} 
    who will be staying with us for ${motelCustomer.getDurationOfStay()} nights. They prefer 
    ${motelCustomer.roomPreferences.join(", ")} for their room. Check-in: 
    ${motelCustomer.stay.checkIn.toLocaleDateString()}, Check-out: ${motelCustomer.stay.checkOut.toLocaleDateString()}.
    
    Contact: ${motelCustomer.phoneNumber}
    Address: ${Object.values(motelCustomer.mailingAddress).join(", ")}
    
    Payment method: ${motelCustomer.paymentMethod}
    We look forward to providing an excellent stay for our guest!
    `;
    
    console.log(customerDescription);
