import { useState } from 'react'
import Pages from '../pages/Pages'





function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <Pages />
        
      </div>
    </>
  )
}

export default App
