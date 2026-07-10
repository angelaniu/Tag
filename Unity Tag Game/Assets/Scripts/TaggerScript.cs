using UnityEngine;
using UnityEngine.InputSystem;

public class TaggerScript : MonoBehaviour
{
    public Rigidbody2D TaggerBody;
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

        if (Keyboard.current.wKey.isPressed)
        {
            movement.y += 1;
        }
        if (Keyboard.current.sKey.isPressed)
        {
            movement.y -= 1;
        }
        if (Keyboard.current.aKey.isPressed)
        {
            movement.x -= 1;
        }
        if (Keyboard.current.dKey.isPressed)
        {
            movement.x += 1;
        }

        movement = movement.normalized;
        TaggerBody.linearVelocity = movement * MoveSpeed;
    }
}
