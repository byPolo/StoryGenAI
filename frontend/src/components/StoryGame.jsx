import {useState, useEffect} from "react";

function Story({story, onNewStory}) {
    const [currentNodeId, setCurrentNodeId] = useState(null)
    const [currentNode, setCurrentNode] = useState(null)
    const [options, setOptions] = useState([])
    const [isEnding, setIsEnding] = useState(false)
    const [isWinningEnding, setIsWinninigEnding] = useState(false)

    useEffect(() => {
        if (story && story.root_node) {
            const rootNodeId = story.root_node.id
            setCurrentNodeId(rootNodeId)
        }
    }, [story])

    useEffect(() => {
        if (currentNode && story && story.all_nodes) {
            const node = story.all_node[currentNodeId]

            setCurrentNode(node)
            setIsEnding(node.is_ending)
            setIsWinninigEnding(node.is_winning_ending)
        }

        if (!node.is_ending && node.options && node.options.length > 0) {
            setOptions(node.options)
        } else {
            setOptions([])
        }
    }, [currentNodeId, story])

    const restartStory = () => {
        if (story && story.root_node) {
            setCurrentNodeId(story.root_node.id)
        }
    }

    return (
        <div className="story-game">
            <header className="story-header">
                <h2>{story.title}</h2>
            </header>

            <div className="story-content">
                {currentNode && <div className="story-node">
                    <p>{currentNode.content}</p>

                    {isEnding ? (
                        <div className="story-ending">
                            <h3>{isWinningEnding ? "Congratulations" : "The End"}</h3>
                            <p>{isWinningEnding ? "You reached a winning ending" : "Your adventure has ended."}</p>
                        </div>
                    ) : (
                        <div className="story-options">
                            <h3>What will you do?</h3>
                            <div className="options-list">
                                {options.map((option, index) => (
                                    <button key={index} onClick={() => chooseOption(option.node_id)}>{option.text}</button>
                                ))}
                            </div>
                        </div>
                    )}
                </div>}
            </div>

            <div className="story-controls">
                <button onClick={restartStory} className="reset-btn">Restart Story</button>
            </div>

            {onNewStory && <button onClick={onNewStory} className="new-story-btn">New Story</button>}
        </div>
    )
}

export default StoryGame
