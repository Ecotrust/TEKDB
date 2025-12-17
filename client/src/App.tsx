import { useEffect, useMemo, useState } from 'react'
import './App.css'
import { fetchPageContent, type PageContentResponse } from './api/pageContent'

function App() {
  const [pageName, setPageName] = useState<'Welcome' | 'About' | 'Help'>('Welcome')
  const [data, setData] = useState<PageContentResponse | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const controller = useMemo(() => new AbortController(), [pageName])

  useEffect(() => {
    setLoading(true)
    setError(null)
    setData(null)
    fetchPageContent(pageName, controller.signal)
      .then((resp) => setData(resp))
      .catch((e) => {
        if (e.name !== 'AbortError') setError(String(e))
      })
      .finally(() => setLoading(false))
    return () => controller.abort()
  }, [pageName])

  return (
    <>
      <header style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
        <h1 style={{ marginRight: 16 }}>TEKDB</h1>
        <nav style={{ display: 'flex', gap: 8 }}>
          <button
            className={pageName === 'Welcome' ? 'selected' : ''}
            onClick={() => setPageName('Welcome')}
          >
            Home
          </button>
          <button
            className={pageName === 'About' ? 'selected' : ''}
            onClick={() => setPageName('About')}
          >
            About
          </button>
          <button
            className={pageName === 'Help' ? 'selected' : ''}
            onClick={() => setPageName('Help')}
          >
            Help
          </button>
        </nav>
      </header>

      <main style={{ marginTop: 24 }}>
        {loading && <p>Loading…</p>}
        {error && <p style={{ color: 'red' }}>Error: {error}</p>}
        {!loading && !error && data && (
          <article>
            <h2>{data.pageTitle}</h2>
            {/* pageContent may include HTML from admin; rendering as HTML intentionally */}
            <div dangerouslySetInnerHTML={{ __html: data.pageContent }} />
          </article>
        )}
      </main>
    </>
  )
}

export default App
