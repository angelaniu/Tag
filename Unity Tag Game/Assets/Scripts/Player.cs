using UnityEngine;
using UnityEngine.InputSystem;
using UnityEngine.InputSystem.Controls;
using UnityEngine.UI;
using static UnityEngine.GraphicsBuffer;

public class Player:MonoBehaviour
{
    public int playerScore = 0;
    public Rigidbody2D rigidBody;
    public bool tagged = false;
    public float MoveSpeed = 5;
    private KeyControl up;
    private KeyControl down;
    private KeyControl left;
    private KeyControl right;

    public void Awake()
    {
        rigidBody = GetComponent<Rigidbody2D>();
    }
    public void Move()
    {
        if (tagged)
        {
            rigidBody.linearVelocity = Vector2.zero;
            return;
        }

        Vector2 movement = Vector2.zero;

        if (up.isPressed)
            movement.y++;

        if (down.isPressed)
            movement.y--;

        if (left.isPressed)
            movement.x--;

        if (right.isPressed)
            movement.x++;

        rigidBody.linearVelocity = movement.normalized * MoveSpeed;
    }

    public void addScore()
    {
        playerScore++;
    }
    public void SetArrowControls()
    {
        up = Keyboard.current.upArrowKey;
        down = Keyboard.current.downArrowKey;
        left = Keyboard.current.leftArrowKey;
        right = Keyboard.current.rightArrowKey;
    }

    public void SetWasdControls()
    {
        up = Keyboard.current.wKey;
        down = Keyboard.current.sKey;
        left = Keyboard.current.aKey;
        right = Keyboard.current.dKey;
    }
}
