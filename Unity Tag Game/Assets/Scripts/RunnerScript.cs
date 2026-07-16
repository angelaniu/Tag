using System;
using Unity.VisualScripting;
using UnityEngine;
using UnityEngine.InputSystem;
using UnityEngine.UIElements;
using static Unity.Collections.Unicode;

public class RunnerScript : Player
{
    public SpriteRenderer spriteRenderer;
    public LogicScript logic;
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        logic = GameObject.FindGameObjectWithTag("Logic").GetComponent<LogicScript>();
        SetWasdControls();
    }

    // Update is called once per frame
    void Update()
    {
    }

    void FixedUpdate()
    {
        Move();
    }

    private void OnCollisionEnter2D(Collision2D collision)
    {
        if (tagged) return;
        if (collision.gameObject.CompareTag("Tagger"))
        {
            spriteRenderer.color = Color.magenta;
            tagged = true;
            logic.gameOver();
        }
    }
    [ContextMenu("Increase Runner Score")]
    private void IncreaseRunnerScore()
    {
        addScore();
    }
}
