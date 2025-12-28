const fs = require('fs');
const path = require('path');

const parser = (filePath) => {
    const data = fs.readFileSync(filePath, 'utf8');
    const lines = data.split('\n');
    const features = [];

    lines.forEach((line) => {
        const columns = line.trim().split(/\s+/);
        features.push(columns.slice(0, -1));
    });

    return {
        features,
        labels: lines.map((line) => line.trim().split(/\s+/).pop()),
    };
};

module.exports = parser;