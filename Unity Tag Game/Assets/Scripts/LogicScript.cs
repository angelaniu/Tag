using UnityEngine;
using UnityEngine.SocialPlatforms.Impl;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class LogicScript : MonoBehaviour
{
    public Text TaggerScoreText;
    public Text RunnerScoreText;
    private Player tagger;
    private Player runner;
    public GameObject gameOverScreen;


    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        tagger = new Player("Tagger", TaggerScoreText);
        runner = new Player("Runner", RunnerScoreText);
    }

    // Update is called once per frame
    void Update()
    {

    }

    [ContextMenu("Increase Tagger Score")]
    private void IncreaseTaggerScore()
    {
        tagger.addScore();
    }

    [ContextMenu("Increase Runner Score")]
    private void IncreaseRunnerScore()
    {
        runner.addScore();
    }
    public void restartGame()
    {
        SceneManager.LoadScene(SceneManager.GetActiveScene().name);
    }

    public void gameOver()
    {
        gameOverScreen.SetActive(true);
    }
}
