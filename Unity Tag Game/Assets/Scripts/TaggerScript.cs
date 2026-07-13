using UnityEngine;
using UnityEngine.InputSystem;

public class TaggerScript : MonoBehaviour
{
    public Rigidbody2D TaggerBody;
    public float MoveSpeed;
    public bool tagged = false;
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
        if (!tagged)
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
        else
        {
            TaggerBody.linearVelocity = Vector2.zero;
        }
    }

    public void OnCollisionEnter2D(Collision2D collision)
    {
        if (tagged) return;
        if (collision.gameObject.CompareTag("Runner")){
            tagged = true;
        }
    }
}
