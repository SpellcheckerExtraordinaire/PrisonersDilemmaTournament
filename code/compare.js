const names = ['FallenAngel', 'FallenAngel2', 'Priest', 'AngryPriest'];
const COLSIZE = 30;

const data = require('./results.json');

for (let i in data) {
  data[i].playerA.name = data[i].playerA.name.replace(/[a-zA-Z0-9]+\./, '');
  data[i].playerB.name = data[i].playerB.name.replace(/[a-zA-Z0-9]+\./, '');

  //console.log(data[i].playerA.name);
  //console.log(data[i].playerB.name);
}

function standardDeviation(a) {
  let mean = 0;
  a.map(a => mean += a);
  mean /= a.length;

  let sum = 0;
  for (let val of a) {
    sum += (val - mean) * (val - mean);
  }
  return Math.sqrt(1 / a.length * sum);
}

function compare(data, names) {
  let relevant = [];
  let participants = [];
  let participantStuff = {};
  for (let i in data) {
    if (names.indexOf(data[i].playerA.name) >= 0) {
      relevant.push(data[i]);
      if (participants.indexOf(data[i].playerB.name) < 0) {
        participants.push(data[i].playerB.name);
        participantStuff[data[i].playerB.name] = {};
      }
      participantStuff[data[i].playerB.name][data[i].playerA.name]=data[i].playerA.avgScore;
    }
    if (names.indexOf(data[i].playerB.name) >= 0) {
      relevant.push(data[i]);
      if (participants.indexOf(data[i].playerA.name) < 0) {
        participants.push(data[i].playerA.name);
        participantStuff[data[i].playerA.name] = {};
      }
      participantStuff[data[i].playerA.name][data[i].playerB.name]=data[i].playerB.avgScore;
    }
  }

  for(let i in names){
    participants.splice(participants.indexOf(names[i]),1);
  }

  function mapParticipants(a) {
    let ar = [];
    for(let v in participantStuff[a]){
      ar.push(participantStuff[a][v]);
    }
    return [a, standardDeviation(ar)];
  }

  participants = participants.map(mapParticipants).sort((a, b) => b[1] - a[1]).map(a => a[0]);

  let t1 =  "Opponent ".padStart(COLSIZE);
  let t2 = "---------".padStart(COLSIZE,'-');

  for(let n in names){
    t1 += "|"+names[n].padEnd(COLSIZE);
    t2 += "+"+"".padEnd(COLSIZE,"-");
  }

  console.log(`${t1}\n${t2}`);
  for(let i in participants){
    let t = '';
    for(let n in names){
      t += ("| "+Math.round(participantStuff[participants[i]][names[n]]*1000)/1000).padEnd(COLSIZE+1);
    }
    console.log(`${(''+participants[i]).padEnd(COLSIZE)}${t}`);
  }
}

compare(data, names)