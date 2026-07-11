using Unity.VisualScripting;
using UnityEngine;
using UnityEngine.InputSystem;
using UnityEngine.UIElements;

public class RunnerScript : MonoBehaviour
{
    public Rigidbody2D RunnerBody;
    public float MoveSpeed;
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
    }

    void FixedUpdate()
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

    private void OnCollisionEnter2D(Collision2D collision)
    {
        //Die
    }
}
