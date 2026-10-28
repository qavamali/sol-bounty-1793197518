import React, { useState, useEffect, useRef } from 'react';
import { 
  Twitter, 
  Video, 
  FileText, 
  Share2, 
  Copy, 
  Check, 
  ExternalLink, 
  Play, 
  Pause, 
  RotateCcw, 
  Coins, 
  Award, 
  ChevronRight, 
  Eye, 
  Bookmark, 
  Sparkles,
  Zap,
  TrendingUp,
  Globe,
  Flame,
  ArrowUpRight
} from 'lucide-react';

export default function KriptoKCreatorHub() {
  const [activeTab, setActiveTab] = useState('thread');
  const [copiedId, setCopiedId] = useState(null);
  
  // Teleprompter state for video script
  const [isPlaying, setIsPlaying] = useState(false);
  const [scrollSpeed, setScrollSpeed] = useState(1.5);
  const teleprompterRef = useRef(null);

  // Copy helper
  const handleCopy = (text, id) => {
    navigator.clipboard.writeText(text);
    setCopiedId(id);
    setTimeout(() => setCopiedId(null), 2500);
  };

  // Teleprompter autoscroll effect
  useEffect(() => {
    let interval = null;
    if (isPlaying) {
      interval = setInterval(() => {
        if (teleprompterRef.current) {
          teleprompterRef.current.scrollTop += scrollSpeed;
          if (
            teleprompterRef.current.scrollTop + teleprompterRef.current.clientHeight >=
            teleprompterRef.current.scrollHeight
          ) {
            setIsPlaying(false);
          }
        }
      }, 30);
    } else {
      clearInterval(interval);
    }
    return () => clearInterval(interval);
  }, [isPlaying, scrollSpeed]);

  const twitterThread = [
    {
      id: "t1",
      number: "1/10",
      content: `Crypto moves at lightspeed, but 99% of people are still left behind by jargon and gatekeeping. 🛑\n\nMeet @KriptoK — the community-driven media powerhouse reshaping Web3 education on Solana.\n\nHere is how they are onboarding the next 100M users into crypto (and why creators are winning): 🧵👇`
    },
    {
      id: "t2",
      number: "2/10",
      content: `The fundamental problem with crypto content today:\n\n❌ Boring 40-page whitepapers nobody reads\n❌ High gas fees preventing micro-tips for creators\n❌ Algorithmic suppression of crypto topics on traditional Web2 platforms\n\nKriptoK bridges this gap with hyper-engaging, bite-sized education. 💡`
    },
    {
      id: "t3",
      number: "3/10",
      content: `Why build on @Solana?\n\nSpeed and micropayments. ⚡\n\nOn Solana, tipping a creator $0.05 in $USDC costs a fraction of a cent and settles in 400ms.\n\nTraditional Web2 takes 30-50% cuts. KriptoK leverages on-chain rails so 100% of community support reaches creators directly.`
    },
    {
      id: "t4",
      number: "4/10",
      content: `Education meets Gamification 🎮\n\nLearning crypto shouldn't feel like studying for a calculus exam.\n\nKriptoK transforms DeFi mechanics, wallet security, and staking into interactive short-form media, actionable guides, and incentivized creator challenges.`
    },
    {
      id: "t5",
      number: "5/10",
      content: `The 200 USDC Creator Challenge isn't just a giveaway.\n\nIt is proof of concept for the decentralized creator economy:\n1️⃣ Produce high-value Web3 content\n2️⃣ Get evaluated transparently via @SuperteamEarn\n3️⃣ Receive instant on-chain bounty payouts in stablecoins\n\nNo intermediaries. Zero invoices. Instant settlement.`
    },
    {
      id: "t6",
      number: "6/10",
      content: `Core verticals KriptoK covers:\n\n🔹 Solana Ecosystem Alpha (DeFi, DePIN, Consumer Apps)\n🔹 Security 101 (Cold storage, hardware keys, anti-phishing)\n🔹 Tokenomics breakdown without the fluff\n🔹 Step-by-step onboarding for non-crypto natives`
    },
    {
      id: "t7",
      number: "7/10",
      content: `Let's talk engagement metrics. 📈\n\nShort-form visual media produces up to 4x higher retention than static text.\n\nBy uniting short-form visual storytelling with Solana's mobile stack (SMS & Saga ecosystem), KriptoK places crypto literacy directly into millions of pockets.`
    },
    {
      id: "t8",
      number: "8/10",
      content: `How can YOU participate in the KriptoK ecosystem?\n\n1. Follow @KriptoK & explore community content\n2. Join active creator bounties on @SuperteamEarn\n3. Publish research, videos, and threads breaking down key Solana narratives\n4. Earn USDC directly to your Phantom/Backpack wallet`
    },
    {
      id: "t9",
      number: "9/10",
      content: `Web3 will not achieve mainstream adoption through complex technical documentation alone.\n\nIt happens when passionate storytellers translate complex decentralization into accessible, viral education.\n\nThat is the exact mission KriptoK is executing every single day. 🚀`
    },
    {
      id: "t10",
      number: "10/10",
      content: `Are you ready to join the creator revolution with KriptoK?\n\nRT the first tweet if you learned something new! 🔁\nBookmark this thread for later! 🔖\nDrop your thoughts below: What topic should KriptoK tackle next? 👇\n\n#Solana #KriptoK #Web3Education #CryptoCreators`
    }
  ];

  const fullThreadText = twitterThread.map(t => `${t.number}\n${t.content}`).join('\n\n---\n\n');

  const videoScript = {
    title: "How KriptoK is Making Crypto 10x Easier (60-Second Viral Short)",
    duration: "60 Seconds",
    format: "9:16 Vertical Video (TikTok / YouTube Shorts / IG Reels)",
    audioRecommendation: "Upbeat Lo-Fi or Electronic Synthwave (Trending Web3 Audio)",
    scenes: [
      {
        time: "0:00 - 0:04",
        hook: "HOOK (High Energy)",
        visual: "Creator holds phone showing a confusing 80-page crypto whitepaper, shaking their head. Fast camera zoom in.",
        spoken: "Crypto was supposed to be the future of money... so why does learning it feel like reading rocket science?",
        sound: "Whoosh sound effect + dramatic stop"
      },
      {
        time: "0:04 - 0:15",
        hook: "THE PAIN POINT",
        visual: "Quick montage of failed transactions, high gas fee warnings on screen, and confusing discord chats.",
        spoken: "Between 50-dollar gas fees and confusing terminology, 95% of newcomers quit before buying their first digital asset.",
        sound: "Record scratch + subtle bass drop"
      },
      {
        time: "0:15 - 0:28",
        hook: "THE SOLUTION: KRIPTOK",
        visual: "Seamless cut to KriptoK logo animation on Solana. Fast-paced, clean UI screens showing micro-learning modules.",
        spoken: "Enter KriptoK. They are stripping away the jargon and replacing it with bite-sized, high-signal education built directly on Solana.",
        sound: "Upbeat electronic rhythm kicks in"
      },
      {
        time: "0:28 - 0:42",
        hook: "WHY SOLANA POWERS THIS",
        visual: "Split screen: Solana transaction completing in 0.4 seconds with a 0.00025 fee vs. happy creator receiving an on-chain tip.",
        spoken: "Because on Solana, transactions cost fractions of a cent and confirm in 400 milliseconds. That means creators get tipped instantly with zero middleman cuts.",
        sound: "Chime / Cash register sound effect"
      },
      {
        time: "0:42 - 0:54",
        hook: "CREATOR OPPORTUNITY",
        visual: "Show Superteam Earn bounty page: '200 USDC Creator Challenge' with glowing cursor clicking submit.",
        spoken: "Right now, they're running a 200 USDC challenge for creators to share knowledge, create content, and get rewarded on-chain.",
        sound: "Tension riser"
      },
      {
        time: "0:54 - 1:00",
        hook: "STRONG CTA",
        visual: "Creator points down to screen; text overlay: 'Join KriptoK on Superteam Earn & follow for daily alpha'.",
        spoken: "Stop struggling through boring whitepapers. Follow KriptoK and start learning Web3 the smart way today!",
        sound: "Outro ding + music swell"
      }
    ]
  };

  const longFormArticle = {
    title: "Demystifying Web3: How KriptoK and Solana are Rebuilding the Decentralized Creator Economy",
    readingTime: "5 min read",
    author: "Web3 Technical Strategist",
    sections: [
      {
        heading: "1. The Grand Paradox of Web3 Adoption",
        body: `For over a decade, blockchain proponents have predicted the inevitable transition from centralized platform feudalism (Web2) to user-owned sovereignty (Web3). Yet, despite trillions in market capitalization and unprecedented developer interest, mainstream consumer onboarding remains stubbornly sluggish.\n\nThe roadblock is not a lack of technological throughput—modern Layer-1 networks like Solana have systematically solved the trilemma by delivering 2,000+ real-time TPS with sub-second deterministic finality. The true bottleneck is educational friction and broken creator economics.`
      },
      {
        heading: "2. The Friction Point in Contemporary Crypto Media",
        body: `Traditional media outlets fail crypto newcomers in two distinct ways:\n\n1. Technical Esotericism: Content is either written for cryptographic researchers or PhD-level financial engineers.\n2. Speculative Sensationalism: Mainstream media fixates on fleeting price volatility rather than architectural utility and decentralized sovereign identity.\n\nFurthermore, Web2 distribution platforms enforce an adversarial model against creators: demonetization algorithms, 30% to 50% revenue extractions, and arbitrary account censorship. Content creators who educate the public about decentralization are paradoxically trapped in centralized systems.`
      },
      {
        heading: "3. The KriptoK Paradigm: Micro-Learning on Solana Rails",
        body: `KriptoK is engineered to resolve both sides of this equation. By restructuring blockchain education into modular, digestible, and culturally resonant formats, KriptoK transforms passive viewers into educated, proactive on-chain participants.\n\nCrucially, by anchoring its ecosystem to Solana, KriptoK enables true micropayments. When micro-donations and content bounties can be settled for $0.00025 per transaction in USDC, the traditional barrier between creator and consumer evaporates. A consumer can tip a creator $0.10 for a high-value security tip without transaction overhead eating 200% of the value.`
      },
      {
        heading: "4. The 200 USDC Creator Challenge as an Economic Template",
        body: `The 200 USDC Creator Challenge hosted through Superteam Earn exemplifies this modern mechanism design. Rather than relying on speculative token handouts, KriptoK utilizes performance-based, meritocratic micro-grants.\n\nCreators are incentivized to produce original, high-signal content that explains the fundamentals of Web3 and the Solana ecosystem. The deliverables undergo peer and community review, and bounties are disbursed directly to non-custodial Solana wallets in USDC—verifiable on-chain on Solscan with zero intermediary friction.`
      },
      {
        heading: "5. Conclusion: The Path Forward",
        body: `The next billion Web3 users will not be onboarded by whitepapers; they will be onboarded by relatable, engaging content creators wielding decentralized infrastructure. Through focused educational campaigns, transparent community bounties, and Solana's lightning-fast throughput, KriptoK is laying down the educational foundation for a truly open financial internet.`
      }
    ]
  };

  const infographicIdeas = [
    {
      title: "Infographic 1: Solana vs. Traditional Web2 Creator Economics",
      type: "Comparison Chart",
      dimensions: "1080 x 1350 px (Instagram / LinkedIn Carousel format)",
      elements: [
        "Left Column: Web2 Social Platforms (Takes 30-50% cut, 30-day payout delay, minimum $100 payout threshold, subject to demonetization).",
        "Right Column: KriptoK on Solana (100% direct p2p tips, 400ms instant settlement, no minimum payout, immune to arbitrary bank freezes).",
        "Visual Anchor: Split-screen graphic with vibrant Solana purple/green glowing metrics vs dull grey Web2 metrics."
      ]
    },
    {
      title: "Infographic 2: The 5-Step Web3 Onboarding Funnel with KriptoK",
      type: "Roadmap / Flowchart",
      dimensions: "1200 x 675 px (Twitter Card format)",
      elements: [
        "Step 1: Watch 60-second KriptoK bite-sized security guide.",
        "Step 2: Install Phantom / Backpack non-custodial wallet safely.",
        "Step 3: Secure 12-word seed phrase offline (zero screenshots).",
        "Step 4: Receive first micro-reward in USDC on Solana.",
        "Step 5: Participate in Superteam Earn bounties and become a creator."
      ]
    },
    {
      title: "Meme Blueprint: 'Reading the Whitepaper vs. KriptoK 60-Second Breakdown'",
      type: "Viral Meme Layout",
      dimensions: "1080 x 1080 px",
      elements: [
        "Top Panel: Person sweating profusely staring at 50 pages of mathematical proof with caption: 'Trying to understand DeFi in 2020'.",
        "Bottom Panel: Relaxed person drinking coffee watching KriptoK on their phone with caption: 'Understanding Solana in 60 seconds with KriptoK'."
      ]
    }
  ];

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 flex flex-col font-sans selection:bg-purple-600 selection:text-white">
      {/* Top Banner */}
      <header className="border-b border-slate-800 bg-slate-900/60 backdrop-blur-md sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-purple-600 via-indigo-500 to-emerald-400 p-[2px] flex items-center justify-center shadow-lg shadow-purple-500/20">
              <div className="w-full h-full bg-slate-950 rounded-[10px] flex items-center justify-center">
                <Zap className="w-5 h-5 text-emerald-400" />
              </div>
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="font-extrabold text-lg tracking-tight bg-gradient-to-r from-purple-400 via-indigo-300 to-emerald-400 bg-clip-text text-transparent">
                  KriptoK
                </span>
                <span className="text-xs px-2 py-0.5 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 font-medium">
                  200 USDC Challenge
                </span>
              </div>
              <p className="text-[11px] text-slate-400">Content Engine & Creator Suite on Solana</p>
            </div>
          </div>

          <div className="flex items-center gap-3">
            <div className="hidden sm:flex items-center gap-2 px-3 py-1.5 rounded-lg bg-slate-900 border border-slate-800 text-xs text-slate-300">
              <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
              <span>Network: <strong>Solana Mainnet</strong></span>
            </div>
            <a 
              href="https://earn.superteam.fun" 
              target="_blank" 
              rel="noreferrer"
              className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-purple-600 hover:bg-purple-500 text-white text-xs font-semibold transition-all shadow-md shadow-purple-600/30"
            >
              <span>Superteam Earn</span>
              <ArrowUpRight className="w-3.5 h-3.5" />
            </a>
          </div>
        </div>
      </header>

      {/* Hero Header */}
      <section className="relative overflow-hidden pt-12 pb-8 border-b border-slate-800/80 bg-gradient-to-b from-purple-950/20 via-slate-950 to-slate-950">
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_top_right,rgba(147,51,234,0.12),transparent_50%)]"></div>
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
          <div className="flex flex-col md:flex-row md:items-center justify-between gap-6">
            <div className="max-w-2xl">
              <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-purple-500/10 border border-purple-500/30 text-purple-300 text-xs font-medium mb-3">
                <Sparkles className="w-3.5 h-3.5" /> Official Bounty Submission Kit
              </div>
              <h1 className="text-3xl sm:text-4xl font-extrabold tracking-tight text-white">
                Educating the Next 100M Crypto Users with <span className="text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-emerald-400">KriptoK</span>
              </h1>
              <p className="mt-3 text-slate-400 text-sm sm:text-base leading-relaxed">
                Complete, production-ready multimedia content suite including an educational 10-part viral thread, high-retention 60-second video script with interactive teleprompter, long-form manifesto, and campaign visual blueprints.
              </p>
            </div>

            {/* Quick Metrics Badge */}
            <div className="grid grid-cols-3 gap-3 p-4 rounded-xl bg-slate-900/80 border border-slate-800 backdrop-blur-sm">
              <div className="text-center px-2">
                <p className="text-xs text-slate-400">Target Grant</p>
                <p className="text-lg font-bold text-emerald-400">200 USDC</p>
              </div>
              <div className="text-center px-2 border-x border-slate-800">
                <p className="text-xs text-slate-400">Deliverables</p>
                <p className="text-lg font-bold text-purple-400">4 Assets</p>
              </div>
              <div className="text-center px-2">
                <p className="text-xs text-slate-400">Ecosystem</p>
                <p className="text-lg font-bold text-indigo-400">Solana</p>
              </div>
            </div>
          </div>

          {/* Navigation Tabs */}
          <div className="flex items-center gap-2 mt-8 overflow-x-auto pb-2 border-b border-slate-800">
            <button
              onClick={() => setActiveTab('thread')}
              className={`flex items-center gap-2 px-4 py-2.5 rounded-lg text-sm font-medium transition-all whitespace-nowrap ${
                activeTab === 'thread'
                  ? 'bg-purple-600/20 text-purple-300 border border-purple-500/40 shadow-sm'
                  : 'text-slate-400 hover:text-slate-200 hover:bg-slate-900'
              }`}
            >
              <Twitter className="w-4 h-4 text-sky-400" />
              <span>X / Twitter Thread</span>
              <span className="ml-1 text-xs px-1.5 py-0.5 rounded-full bg-slate-800 text-slate-300">10 Parts</span>
            </button>

            <button
              onClick={() => setActiveTab('video')}
              className={`flex items-center gap-2 px-4 py-2.5 rounded-lg text-sm font-medium transition-all whitespace-nowrap ${
                activeTab === 'video'
                  ? 'bg-purple-600/20 text-purple-300 border border-purple-500/40 shadow-sm'
                  : 'text-slate-400 hover:text-slate-200 hover:bg-slate-900'
              }`}
            >
              <Video className="w-4 h-4 text-rose-400" />
              <span>Viral 60s Script + Teleprompter</span>
            </button>

            <button
              onClick={() => setActiveTab('article')}
              className={`flex items-center gap-2 px-4 py-2.5 rounded-lg text-sm font-medium transition-all whitespace-nowrap ${
                activeTab === 'article'
                  ? 'bg-purple-600/20 text-purple-300 border border-purple-500/40 shadow-sm'
                  : 'text-slate-400 hover:text-slate-200 hover:bg-slate-900'
              }`}
            >
              <FileText className="w-4 h-4 text-emerald-400" />
              <span>Deep-Dive Article</span>
            </button>

            <button
              onClick={() => setActiveTab('visuals')}
              className={`flex items-center gap-2 px-4 py-2.5 rounded-lg text-sm font-medium transition-all whitespace-nowrap ${
                activeTab === 'visuals'
                  ? 'bg-purple-600/20 text-purple-300 border border-purple-500/40 shadow-sm'
                  : 'text-slate-400 hover:text-slate-200 hover:bg-slate-900'
              }`}
            >
              <Sparkles className="w-4 h-4 text-amber-400" />
              <span>Visual & Meme Concepts</span>
            </button>
          </div>
        </div>
      </section>

      {/* Main Content Area */}
      <main className="flex-1 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 w-full">
        {/* TAB 1: TWITTER THREAD */}
        {activeTab === 'thread' && (
          <div className="space-y-6">
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 p-4 rounded-xl bg-slate-900/60 border border-slate-800">
              <div>
                <h2 className="text-base font-semibold text-white flex items-center gap-2">
                  <Twitter className="w-5 h-5 text-sky-400" />
                  X/Twitter Mega-Thread: KriptoK x Solana Architecture
                </h2>
                <p className="text-xs text-slate-400 mt-1">
                  Engineered with viral hooks, sub-second finality data, and audience conversion loops.
                </p>
              </div>
              <button
                onClick={() => handleCopy(fullThreadText, 'full-thread')}
                className="flex items-center justify-center gap-2 px-4 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-200 transition-all border border-slate-700"
              >
                {copiedId === 'full-thread' ? (
                  <>
                    <Check className="w-4 h-4 text-emerald-400" />
                    <span>Copied Entire Thread!</span>
                  </>
                ) : (
                  <>
                    <Copy className="w-4 h-4 text-slate-400" />
                    <span>Copy Full Thread</span>
                  </>
                )}
              </button>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              {twitterThread.map((tweet) => (
                <div 
                  key={tweet.id} 
                  className="p-5 rounded-xl bg-slate-900/40 border border-slate-800/80 hover:border-purple-500/30 transition-all flex flex-col justify-between relative group"
                >
                  <div>
                    <div className="flex items-center justify-between mb-3">
                      <span className="text-xs font-mono font-bold text-purple-400 px-2 py-0.5 rounded bg-purple-950/60 border border-purple-800/50">
                        {tweet.number}
                      </span>
                      <button
                        onClick={() => handleCopy(tweet.content, tweet.id)}
                        className="text-slate-400 hover:text-white p-1 rounded-md hover:bg-slate-800 transition"
                        title="Copy this tweet"
                      >
                        {copiedId === tweet.id ? (
                          <Check className="w-4 h-4 text-emerald-400" />
                        ) : (
                          <Copy className="w-4 h-4" />
                        )}
                      </button>
                    </div>
                    <p className="text-sm text-slate-300 whitespace-pre-line leading-relaxed">
                      {tweet.content}
                    </p>
                  </div>
                  <div className="mt-4 pt-3 border-t border-slate-800/60 flex items-center justify-between text-xs text-slate-400">
                    <span>{tweet.content.length} characters</span>
                    <span className="text-slate-400 group-hover:text-purple-400 transition">Ready to Tweet</span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* TAB 2: VIDEO SCRIPT & TELEPROMPTER */}
        {activeTab === 'video' && (
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            {/* Left 2 Cols: Interactive Teleprompter & Scenes */}
            <div className="lg:col-span-2 space-y-6">
              <div className="p-4 rounded-xl bg-slate-900/60 border border-slate-800 flex flex-wrap items-center justify-between gap-4">
                <div>
                  <h2 className="text-base font-semibold text-white flex items-center gap-2">
                    <Video className="w-5 h-5 text-rose-400" />
                    {videoScript.title}
                  </h2>
                  <p className="text-xs text-slate-400 mt-0.5">
                    {videoScript.duration} • {videoScript.format}
                  </p>
                </div>
                
                {/* Teleprompter Controls */}
                <div className="flex items-center gap-2">
                  <button
                    onClick={() => setIsPlaying(!isPlaying)}
                    className={`flex items-center gap-2 px-3 py-1.5 rounded-lg text-xs font-semibold transition ${
                      isPlaying 
                        ? 'bg-rose-600 text-white' 
                        : 'bg-emerald-600 hover:bg-emerald-500 text-white'
                    }`}
                  >
                    {isPlaying ? <Pause className="w-3.5 h-3.5" /> : <Play className="w-3.5 h-3.5" />}
                    <span>{isPlaying ? 'Pause Prompter' : 'Start Prompter'}</span>
                  </button>

                  <button
                    onClick={() => {
                      if (teleprompterRef.current) teleprompterRef.current.scrollTop = 0;
                      setIsPlaying(false);
                    }}
                    className="p-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300"
                    title="Reset to Top"
                  >
                    <RotateCcw className="w-4 h-4" />
                  </button>

                  <div className="flex items-center gap-1.5 text-xs text-slate-400 ml-2">
                    <span>Speed:</span>
                    <input 
                      type="range" 
                      min="0.5" 
                      max="3.5" 
                      step="0.5" 
                      value={scrollSpeed} 
                      onChange={(e) => setScrollSpeed(parseFloat(e.target.value))}
                      className="w-16 accent-purple-500"
                    />
                    <span className="font-mono text-purple-300">{scrollSpeed}x</span>
                  </div>
                </div>
              </div>

              {/* Scrolling Teleprompter Box */}
              <div 
                ref={teleprompterRef}
                className="h-[520px] overflow-y-auto space-y-4 p-5 rounded-2xl bg-slate-950 border-2 border-slate-800 relative scroll-smooth shadow-inner"
              >
                {videoScript.scenes.map((scene, idx) => (
                  <div 
                    key={idx}
                    className="p-4 rounded-xl bg-slate-900/70 border border-slate-800/80 hover:border-rose-500/30 transition"
                  >
                    <div className="flex items-center justify-between mb-2">
                      <div className="flex items-center gap-2">
                        <span className="text-xs font-mono font-bold px-2 py-0.5 rounded bg-rose-500/10 text-rose-400 border border-rose-500/20">
                          {scene.time}
                        </span>
                        <span className="text-xs font-semibold uppercase tracking-wider text-slate-400">
                          {scene.hook}
                        </span>
                      </div>
                      <span className="text-[11px] text-slate-400 font-mono flex items-center gap-1">
                        🔊 {scene.sound}
                      </span>
                    </div>

                    <div className="my-2 p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-xs text-slate-400">
                      <strong className="text-slate-300">B-Roll / Visual:</strong> {scene.visual}
                    </div>

                    <div className="p-3 rounded-lg bg-purple-950/20 border border-purple-900/30">
                      <p className="text-sm font-medium text-purple-100 leading-relaxed">
                        🗣️ <span className="font-bold">Voiceover:</span> "{scene.spoken}"
                      </p>
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* Right 1 Col: Production Guide & Script Meta */}
            <div className="space-y-4">
              <div className="p-5 rounded-xl bg-slate-900/60 border border-slate-800">
                <h3 className="text-sm font-bold text-white mb-3 flex items-center gap-2">
                  <Flame className="w-4 h-4 text-amber-400" />
                  Creator Audio & Viral Guidelines
                </h3>
                <ul className="text-xs text-slate-300 space-y-2.5">
                  <li className="flex items-start gap-2">
                    <span className="text-emerald-400">✓</span>
                    <span><strong>Audio Track:</strong> {videoScript.audioRecommendation}</span>
                  </li>
                  <li className="flex items-start gap-2">
                    <span className="text-emerald-400">✓</span>
                    <span><strong>Pacing:</strong> 140–150 words per minute to match TikTok/Reels retention curve.</span>
                  </li>
                  <li className="flex items-start gap-2">
                    <span className="text-emerald-400">✓</span>
                    <span><strong>Text Captions:</strong> Render dynamic kinetic subtitles with yellow/green emphasis on keywords like <em>Solana</em>, <em>KriptoK</em>, and <em>Zero Fees</em>.</span>
                  </li>
                  <li className="flex items-start gap-2">
                    <span className="text-emerald-400">✓</span>
                    <span><strong>Thumbnail Hook:</strong> "Crypto without the headaches" or "How to earn on Solana".</span>
                  </li>
                </ul>

                <button
                  onClick={() => {
                    const scriptText = videoScript.scenes.map(s => `[${s.time}] ${s.hook}\nVisual: ${s.visual}\nAudio: ${s.spoken}`).join('\n\n');
                    handleCopy(scriptText, 'video-script');
                  }}
                  className="w-full mt-4 flex items-center justify-center gap-2 py-2 rounded-lg bg-purple-600 hover:bg-purple-500 text-white text-xs font-semibold transition"
                >
                  {copiedId === 'video-script' ? (
                    <>
                      <Check className="w-4 h-4 text-emerald-400" />
                      <span>Copied Raw Script!</span>
                    </>
                  ) : (
                    <>
                      <Copy className="w-4 h-4" />
                      <span>Copy Full Production Script</span>
                    </>
                  )}
                </button>
              </div>

              {/* Solana Onboarding Callout */}
              <div className="p-4 rounded-xl bg-gradient-to-br from-indigo-950/40 to-purple-950/40 border border-indigo-800/40">
                <p className="text-xs font-semibold text-indigo-300 mb-1 flex items-center gap-1.5">
                  <Coins className="w-4 h-4 text-emerald-400" /> Micro-Tipping Incentive
                </p>
                <p className="text-xs text-slate-300 leading-relaxed">
                  Include your <strong>Solana Domain (.sol)</strong> or wallet public key in the video description to demonstrate native tipping enabled by KriptoK.
                </p>
              </div>
            </div>
          </div>
        )}

        {/* TAB 3: LONG-FORM ARTICLE */}
        {activeTab === 'article' && (
          <div className="max-w-4xl mx-auto space-y-6">
            <div className="p-6 rounded-2xl bg-slate-900/60 border border-slate-800">
              <div className="flex items-center gap-2 text-xs font-medium text-emerald-400 mb-2">
                <span>Medium / Mirror / Substack Ready</span>
                <span>•</span>
                <span>{longFormArticle.readingTime}</span>
              </div>
              <h2 className="text-2xl sm:text-3xl font-extrabold text-white leading-tight">
                {longFormArticle.title}
              </h2>
              <div className="flex items-center justify-between border-b border-slate-800 pb-4 mt-3">
                <p className="text-xs text-slate-400">By {longFormArticle.author}</p>
                <button
                  onClick={() => {
                    const fullArticle = `${longFormArticle.title}\n\n` + longFormArticle.sections.map(s => `${s.heading}\n\n${s.body}`).join('\n\n');
                    handleCopy(fullArticle, 'article-copy');
                  }}
                  className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-medium text-slate-300 transition"
                >
                  {copiedId === 'article-copy' ? <Check className="w-3.5 h-3.5 text-emerald-400" /> : <Copy className="w-3.5 h-3.5" />}
                  <span>Copy Article Markdown</span>
                </button>
              </div>

              <div className="mt-6 space-y-6 text-slate-300 text-sm sm:text-base leading-relaxed">
                {longFormArticle.sections.map((section, i) => (
                  <div key={i} className="space-y-2">
                    <h3 className="text-lg font-bold text-white tracking-tight">
                      {section.heading}
                    </h3>
                    <p className="whitespace-pre-line text-slate-300/90 text-sm leading-relaxed">
                      {section.body}
                    </p>
                  </div>
                ))}
              </div>
            </div>
          </div>
        )}

        {/* TAB 4: VISUAL & MEME BLUEPRINTS */}
        {activeTab === 'visuals' && (
          <div className="space-y-6">
            <div className="p-4 rounded-xl bg-slate-900/60 border border-slate-800 flex items-center justify-between">
              <div>
                <h2 className="text-base font-semibold text-white flex items-center gap-2">
                  <Sparkles className="w-5 h-5 text-amber-400" />
                  Visual Concepts & Social Media Asset Blueprints
                </h2>
                <p className="text-xs text-slate-400 mt-0.5">
                  Ready-to-design asset blueprints for Canva, Figma, and Photoshop creators.
                </p>
              </div>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              {infographicIdeas.map((item, idx) => (
                <div 
                  key={idx}
                  className="p-5 rounded-xl bg-slate-900/40 border border-slate-800 hover:border-amber-500/40 transition-all flex flex-col justify-between"
                >
                  <div>
                    <div className="flex items-center justify-between mb-3">
                      <span className="text-[11px] font-mono px-2 py-0.5 rounded bg-amber-500/10 text-amber-300 border border-amber-500/20">
                        {item.type}
                      </span>
                      <span className="text-[11px] text-slate-400">{item.dimensions}</span>
                    </div>

                    <h3 className="text-sm font-bold text-white mb-3">
                      {item.title}
                    </h3>

                    <div className="space-y-2 bg-slate-950/60 p-3 rounded-lg border border-slate-800/80 text-xs text-slate-300">
                      <p className="font-semibold text-slate-400 text-[11px] uppercase tracking-wider">Asset Specs:</p>
                      {item.elements.map((el, elIdx) => (
                        <p key={elIdx} className="leading-relaxed">
                          • {el}
                        </p>
                      ))}
                    </div>
                  </div>

                  <button
                    onClick={() => handleCopy(item.elements.join('\n'), `vis-${idx}`)}
                    className="mt-4 w-full py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs text-slate-300 transition flex items-center justify-center gap-1.5"
                  >
                    {copiedId === `vis-${idx}` ? <Check className="w-3.5 h-3.5 text-emerald-400" /> : <Copy className="w-3.5 h-3.5" />}
                    <span>Copy Blueprint Elements</span>
                  </button>
                </div>
              ))}
            </div>

            {/* Interactive Color Palette Generator */}
            <div className="p-6 rounded-xl bg-slate-900/60 border border-slate-800">
              <h3 className="text-sm font-bold text-white mb-3 flex items-center gap-2">
                <Globe className="w-4 h-4 text-purple-400" />
                Brand Color Palette for KriptoK Content Creators
              </h3>
              <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
                <div className="p-3 rounded-lg bg-[#9945FF] text-white flex flex-col justify-between h-20 shadow-md">
                  <span className="text-xs font-bold">Solana Purple</span>
                  <span className="text-xs font-mono">#9945FF</span>
                </div>
                <div className="p-3 rounded-lg bg-[#14F195] text-slate-950 flex flex-col justify-between h-20 shadow-md">
                  <span className="text-xs font-bold">Solana Green</span>
                  <span className="text-xs font-mono">#14F195</span>
                </div>
                <div className="p-3 rounded-lg bg-[#6366F1] text-white flex flex-col justify-between h-20 shadow-md">
                  <span className="text-xs font-bold">KriptoK Indigo</span>
                  <span className="text-xs font-mono">#6366F1</span>
                </div>
                <div className="p-3 rounded-lg bg-[#0F172A] text-slate-300 border border-slate-700 flex flex-col justify-between h-20 shadow-md">
                  <span className="text-xs font-bold">Deep Space Slate</span>
                  <span className="text-xs font-mono">#0F172A</span>
                </div>
              </div>
            </div>
          </div>
        )}
      </main>

      {/* Footer / Bounty Credentials */}
      <footer className="border-t border-slate-800/80 bg-slate-950 py-6 mt-12 text-xs text-slate-500">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row items-center justify-between gap-4">
          <div className="flex items-center gap-2">
            <span className="w-2 h-2 rounded-full bg-purple-500"></span>
            <span>Created for the <strong>KriptoK 200 USDC Creator Challenge</strong> on Superteam Earn</span>
          </div>
          <div className="flex items-center gap-4 text-slate-400">
            <span>Built on Solana</span>
            <span>•</span>
            <span>Zero-Gas Micro-Tipping Ready</span>
            <span>•</span>
            <span>MIT Open Source</span>
          </div>
        </div>
      </footer>
    </div>
  );
}