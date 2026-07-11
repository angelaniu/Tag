using UnityEngine;
using UnityEngine.UI;

public class Player:MonoBehaviour
{
    public string playerName;
    public int playerScore;
    public Text playerScoreText;

    public Player(string name, Text scoreText)
    {
        playerName = name;
        playerScore = 0;
        playerScoreText = scoreText;
    }

    public void addScore()
    {
        playerScore++;
        playerScoreText.text = playerScore.ToString();
    }
}
