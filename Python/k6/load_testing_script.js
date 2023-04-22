import http from 'k6/http';
import { sleep } from 'k6';
import { randomItem } from 'https://jslib.k6.io/k6-utils/1.2.0/index.js';

const numDocs = 511;
const textData = []
for(var i = 100; i <= numDocs; i++)
{
    var fileName = i + '.txt'
    var filePath = 'bbc/sport/' + fileName
    
    const textToSend = open(filePath);

    textData.push(textToSend);
}


export const options = {
    scenarios: {
      spike: {
        executor: "ramping-arrival-rate",
        preAllocatedVUs: 1000,
        timeUnit: "1s",
        stages: [
          { duration: "10s", target: 10 },
          { duration: "10s", target: 40 },
          { duration: "10s", target: 0 },
        ],
      },
    },
  };


export default function() {

    // Get page
    let res = http.get('http://127.0.0.1:8080/');
    
    // Add text to form
    res = res.submitForm({
        formSelector: 'form',
        fields: {content: randomItem(textData)},
    });
}