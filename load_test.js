import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
    vus: 10, // 10 virtual users
    duration: '10s', // Test runs for 10 seconds
};

export default function () {
    let res = http.get('http://127.0.0.1:5000'); // Replace with your Flask API endpoint

    check(res, {
        'is status 200': (r) => r.status === 200,
        'response time < 200ms': (r) => r.timings.duration < 200,
    });

    sleep(1); // Simulates user wait time
}
