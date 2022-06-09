const Traveller = function(journeys) {
  this.journeys = journeys;
};

Traveller.prototype.getJourneyStartLocations = function() {
  return this.journeys.map ((journey) => {
    return journey.startLocation;
  });
};

Traveller.prototype.getJourneyEndLocations = function () {
  return this.journeys.map((journey) => {
    return journey.endLocation;
  })
};

Traveller.prototype.getJourneysByTransport = function (transport) {
  return result = this.journeys.filter((journey) => {
  return journey.transport === transport;
  })
};

Traveller.prototype.getJourneysByMinDistance = function (minDistance) {
  return result = this.journeys.filter((journey) => {
    return journey.distance >= minDistance;
  })
};

Traveller.prototype.calculateTotalDistanceTravelled = function () {
  let result = this.journeys.reduce((totalDistance, journey) => {
  return totalDistance + journey.distance; 
  }, 0);
  return result;
};

Traveller.prototype.getUniqueModesOfTransport = function () {

};


module.exports = Traveller;
