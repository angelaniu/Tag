using UnityEngine;
using UnityEngine.InputSystem;

public class TaggerScript : Player
{

    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        SetArrowControls();
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    void FixedUpdate()
    {
        Move();
    }

    public void OnCollisionEnter2D(Collision2D collision)
    {
        if (tagged) return;
        if (collision.gameObject.CompareTag("Runner")){
            tagged = true;
        }
    }
    [ContextMenu("Increase Tagger Score")]
    private void IncreaseTaggerScore()
    {
        addScore();
    }

}
