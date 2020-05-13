// Get player's mastery stats from LoL API
function getChampionStats(summonerName, nameList, region) {
  return new Promise(resolve => {
    var masteryStats = "http://localhost:5000/api/" + region + "/" + summonerName // custom API endpoint with server-side request handling
    //var masteryStats = "https://euw1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedSummonerId}?api={apiKey}"
    $.getJSON(masteryStats, function(masteryList) {
      for (var x in masteryList) {
        var championId = masteryList[x].championId;
        var championName = getChampionName(nameList, championId);
        var championLevel = masteryList[x].championLevel;
        var championPoints = masteryList[x].championPoints;
        var pointsToNextLevel = masteryList[x].championPointsUntilNextLevel;
        var chestGranted = masteryList[x].chestGranted;
        var chestImage;
        if (chestGranted) {
          chestImage = "<img src='images/hextech-chest.png' width='25px'></img>";
        } else {
          chestImage = "<img src='images/hextech-chest-silhouette.png' width='25px'></img>";
        }
        $(championsList).append(
          "<tr id='" + championId + "'>" + 
          "<td>" + championName + "</td>" +
          "<td>" + championLevel + "</td>" +
          "<td>" + championPoints + "</td>" +
          "<td>" + pointsToNextLevel + "</td>" +
          "<td>" + "<span style=display:none>" + chestGranted + "</span>" + chestImage + "</td>" +
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
      var versionNumber = file.n.champion;
      resolve({versionNumber});
    })
  })
}

// Get champion names list from ddragon
function getChampionNamesList(versionNumber) {
  return new Promise(resolve => {
    var championsUrl = "http://ddragon.leagueoflegends.com/cdn/" + versionNumber + "/data/en_US/champion.json"
    $.getJSON(championsUrl, function(file) {
      var championList = file;
      resolve({championList});
    })
  })
}

// Get champion name from list
function getChampionName(nameList, championId) {
  var namesList = nameList.championList.data
  for (var y in namesList) {
    if (namesList[y].key == championId) {
      var name = namesList[y].name;
      return name;
    }
  }
}

// Get chest status
const getChestInfo = async function(region, summonerName){
  try {
    const latestVersion = await getLatestVersion(region);
    const championNamesList = await getChampionNamesList(latestVersion.versionNumber);
    const masteryStats = await getChampionStats(summonerName, championNamesList, region);
  }catch (e){
      //handle errors as needed
      console.log("Error")
  }
}
