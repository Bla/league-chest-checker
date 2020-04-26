// Get player's mastery stats from LoL API
function getChampionStats(summonerName, nameList) {
  return new Promise(resolve => {
    var masteryStats = "http://localhost:5000/api/" + summonerName // custom API endpoint with server-side request handling
    //var masteryStats = "https://euw1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedSummonerId}?api={apiKey}"
    $.getJSON(masteryStats, function(masteryList) {
      for (var x in masteryList) {
          let championId = masteryList[x].championId;
          championName = getChampionName(nameList, championId);
          championLevel = masteryList[x].championLevel;
          championPoints = masteryList[x].championPoints;
          pointsToNextLevel = masteryList[x].championPointsUntilNextLevel;
          chestGranted = masteryList[x].chestGranted;
          $(championsList).append(
            "<tr id='" + championId + "'>" + 
            "<td>" + championName + "</td>" +
            "<td>" + championLevel + "</td>" +
            "<td>" + championPoints + "</td>" +
            "<td>" + pointsToNextLevel + "</td>" +
            "<td>" + chestGranted + "</td>" +
            "</tr>"
            )
      }
      resolve({masteryList});
    })
  })
}

// Get the latest version of the JSON file that contains champion information
function getLatestVersion(region) {
  return new Promise(resolve => {
    var versionsUrl = "https://ddragon.leagueoflegends.com/realms/" + region + ".json";
    $.getJSON(versionsUrl, function(file) {
      versionNumber = file.n.champion;
      document.getElementById("version").innerHTML = versionNumber;
      resolve({versionNumber});
    })
  })
}

// Get champion names list from ddragon
function getChampionNamesList(versionNumber) {
  return new Promise(resolve => {
    var championsUrl = "http://ddragon.leagueoflegends.com/cdn/" + versionNumber + "/data/en_US/champion.json"
    $.getJSON(championsUrl, function(file) {
      championList = file;
      resolve({championList});
    })
  })
}

// Get champion name from list
function getChampionName(nameList, championId) {
  namesList = nameList.championList.data
  for (var y in namesList) {
    if (namesList[y].key == championId) {
      name = namesList[y].name;
      return name;
    }
  }
}

// Get chest status
const getChestInfo = async function(region, summonerName){
  try {
    const latestVersion = await getLatestVersion(region);
    const championNamesList = await getChampionNamesList(latestVersion.versionNumber);
    const masteryStats = await getChampionStats(summonerName, championNamesList);
  }catch (e){
      //handle errors as needed
      console.log("Error")
  }
}
