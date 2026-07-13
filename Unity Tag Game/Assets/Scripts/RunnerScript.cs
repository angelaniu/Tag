using System;
using Unity.VisualScripting;
using UnityEngine;
using UnityEngine.InputSystem;
using UnityEngine.UIElements;

public class RunnerScript : MonoBehaviour
{
    public SpriteRenderer spriteRenderer;
    public Rigidbody2D RunnerBody;
    public float MoveSpeed;
    public bool tagged = false;
    public LogicScript logic;
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        logic = GameObject.FindGameObjectWithTag("Logic").GetComponent<LogicScript>();
    }

    // Update is called once per frame
    void Update()
    {
    }

    void FixedUpdate()
    {
        if (!tagged)
        {
            Vector2 movement = Vector2.zero;

            if (Keyboard.current.upArrowKey.isPressed)
            {
                movement.y += 1;
            }
            if (Keyboard.current.downArrowKey.isPressed)
            {
                movement.y -= 1;
            }
            if (Keyboard.current.leftArrowKey.isPressed)
            {
                movement.x -= 1;
            }
            if (Keyboard.current.rightArrowKey.isPressed)
            {
                movement.x += 1;
            }

            movement = movement.normalized;
            RunnerBody.linearVelocity = movement * MoveSpeed;
        }
        else
        {
            RunnerBody.linearVelocity = Vector2.zero;
        }
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

}
