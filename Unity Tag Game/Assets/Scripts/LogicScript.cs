using UnityEngine;
using UnityEngine.SocialPlatforms.Impl;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class LogicScript : MonoBehaviour
{
    public Text timer;
    public GameObject gameOverScreen;
    public int minutes;
    public int seconds;
    private float time;
    private bool gameStatus;


    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        timer.text = minutes.ToString() + ":" + seconds.ToString("D2");
        gameStatus = true;
    }

    // Update is called once per frame
    void Update()
    {
        time += Time.deltaTime;
        
        if(time >= 1f)
        {
            time -= 1f;
            if (gameStatus)
            {
                countdown();
            }
        }
        if(minutes == 0 && seconds == 0)
        {
            gameOver();
        }
    }

    public void restartGame()
    {
        SceneManager.LoadScene(SceneManager.GetActiveScene().name);
    }

    public void gameOver()
    {
        gameStatus = false;
        gameOverScreen.SetActive(true);
    }

    public void countdown()
    {
        if(seconds == 0){
            minutes--;
            seconds = 60;
        }
        seconds--;
        timer.text = minutes.ToString() + ":" + seconds.ToString("D2");
    }
}

