# CRUV_Assignment
-> Individual players are represented by the Player class, which includes features such as name, bowling skill, batting skill, fielding skill, running skill, and experience.
-> Teams represents the team's players and provides procedures for selecting a captain, selecting a bowler for an over, and deciding the batting order.
-> The Field class depicts a cricket pitch and maintains information like field size, crowd ratio, pitch conditions, and home advantage.
-> The Umpire class accepts a field object and offers methods for predicting a ball's result. It computes probability for each participant based on their talents and provides a random result.
-> The Commentator class delivers commentary for each ball and over.
-> The Match class comprises team, field, umpire, and commentator occurrences. The start_match method runs the simulation by iterating through 6 overs, each with 6 balls. It uses the umpire's predict_outcome_of_ball approach to predict the result of each ball and the commentator's methods to provide commentary.


